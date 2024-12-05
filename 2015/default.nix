let 
  pkgs = import <nixpkgs> {};
in
  pkgs.mkShell {
    packages = with pkgs; [
      R 
      python312 
      python312Packages.jupyter-client 
      rPackages.styler 
      rPackages.testthat 
    ];
  }
