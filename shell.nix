{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.python-frontmatter
      python-pkgs.jinja2
      python-pkgs.markdown
    ]))
  ];

  shellHook = ''
    echo "Python environment loaded!"
    python --version
  '';
}
