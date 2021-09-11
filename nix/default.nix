# https://github.com/nmattia/niv
{ sources ? import ./sources.nix
, nixpkgs ? sources."nixpkgs-21.05"
}:

let

  overlay = _: pkgs: {

    gitignoreSource = (import sources.gitignore {
      inherit (pkgs) lib;
    }).gitignoreSource;

    poetry2nix =
      import (sources.poetry2nix + "/default.nix") {
        pkgs = import sources."nixpkgs-21.05" {};
        poetry = (import sources."nixpkgs-21.05" {}).poetry;
    };

  };

  pkgs = import nixpkgs {
    overlays = [ overlay ];
    config = {};
  };

in pkgs
