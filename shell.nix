{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.nodejs
  ];

  shellHook = ''
    export NPM_CONFIG_PREFIX=$HOME/.npm-global
    export PATH=$NPM_CONFIG_PREFIX/bin:$PATH

    if ! command -v sass-migrator >/dev/null; then
      echo "Installing sass-migrator via npm (user scope)…"
      npm install -g sass-migrator
    fi
  '';
}
