{ supportedSystems ? [ "x86_64-linux" ]
, pkgs ? import (builtins.fetchTarball
  "https://github.com/nixos/nixpkgs-channels/archive/nixos-16.09.tar.gz") {}
, pythonPackages ? pkgs.pythonPackages
}:

let

  pkgFor = system: import ./default.nix {
    pkgs = import pkgs.path { inherit system; };
    inherit pythonPackages;
  };

in rec {

  build = pkgs.lib.genAttrs supportedSystems (system: pkgs.lib.hydraJob (
    pkgFor system
  ));

  python = pkgs.lib.genAttrs supportedSystems (system: pkgs.lib.hydraJob (
    let package = pkgFor system;
        syspkgs = import pkgs.path { inherit system; };
    in syspkgs.pythonPackages.python.buildEnv.override {
      extraLibs = package.nativeBuildInputs
                  ++ package.propagatedNativeBuildInputs;
      ignoreCollisions = true;
    }
  ));

  tarball = pkgs.lib.hydraJob((pkgFor "x86_64-linux")
                    .overrideDerivation(args: {
    phases = [ "unpackPhase" "buildPhase" ];
    buildPhase = ''
      ${python."x86_64-linux"}/bin/python setup.py sdist --formats=gztar
      mkdir -p $out/tarballs $out/nix-support
      mv dist/${args.name}.tar.gz $out/tarballs
      echo "file source-dist $out/tarballs/${args.name}.tar.gz" > \
           $out/nix-support/hydra-build-products
      echo ${args.name} > $out/nix-support/hydra-release-name
    '';
  }));

}
