{ pkgs ? import (builtins.fetchTarball
  "https://github.com/nixos/nixpkgs-channels/archive/nixos-16.09.tar.gz") {}
, pythonPackages ? pkgs.pythonPackages
}:

let self = {
  version = builtins.replaceStrings ["\n"] [""] (builtins.readFile ./VERSION);

  robotframework-selenium2screenshots = pythonPackages.buildPythonPackage {
    name = "robotframework-selenium2screenshots-0.7.0";
    src = pkgs.fetchurl {
      url = "https://pypi.python.org/packages/6f/2c/7be0b687a264dad839fce39f9b28b13b7bf1ebd3b45b3cc858f3c44bc4b9/robotframework-selenium2screenshots-0.7.0.tar.gz";
      sha256 = "64a272e61787ab42206db631a238dae91bccd40a35c47896485c52f0591a4616";
    };
    propagatedBuildInputs = with pythonPackages; [
      pillow
      robotframework-selenium2library
    ];
  };
};

in pythonPackages.buildPythonPackage rec {
  namePrefix = "";
  name = "sphinxcontrib-robotframework-${self.version}";
  src = builtins.filterSource
    (path: type: baseNameOf path != ".git"
              && baseNameOf path != "result")
    ./.;
  buildInputs = with pkgs; with self; with pythonPackages; [
    phantomjs2
    readline
    robotframework-selenium2screenshots
  ];
  propagatedBuildInputs = with pythonPackages; [
    robotframework
    sphinx
  ];
}
