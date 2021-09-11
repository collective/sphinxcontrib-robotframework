{ pkgs ? import ./nix { nixpkgs = sources."nixpkgs-20.09"; }
, sources ? import ./nix/sources.nix {}
, python ? "python38"
, pythonPackages ? builtins.getAttr (python + "Packages") pkgs
}:

let self = {

  version = builtins.replaceStrings ["\n"] [""] (builtins.readFile ./VERSION);

  robotframework-seleniumscreenshots = pythonPackages.buildPythonPackage rec {
    pname = "robotframework-seleniumscreenshots";
    version = "0.9.5";
    src = pythonPackages.fetchPypi {
      inherit pname version;
      sha256 = "05qv323hvjmy62h33ryrjaa9k1hyvp8hq5qnj8j1x3ap2ci3q3s0";
    };
    propagatedBuildInputs = with pythonPackages; [
      pillow
      robotframework-seleniumlibrary
    ];
    doCheck = false;
  };

};

in pythonPackages.buildPythonPackage rec {
  namePrefix = "";
  pname = "sphinxcontrib-robotframework";
  inherit (self) version;
  src = pkgs.gitignoreSource ./.;
  nativeBuildInputs = with self; with pythonPackages; with pkgs; [
    robotframework-seleniumlibrary
    robotframework-seleniumscreenshots
    firefox
    geckodriver
    sphinx
  ];
  propagatedBuildInputs = with pythonPackages; [
    pygments
    robotframework
    sphinx
  ];
  passthru = {
    env = pythonPackages.python.withPackages(ps:
      (nativeBuildInputs ++ propagatedBuildInputs)
    );
  };
}
