#!/usr/bin/env bash
source "$(dirname $0)/conf"

### variables ###
dir="$(tr -dc 'a-zA-Z0-9_=' <<< ${QUERY_STRING} | sed 's;=;s/;')"
md="$contentsdir/$dir/main.md"

[ -f "$md" ]

md="/var/www/bashcms2_contents/posts/20190817_negi/main.md"

### output ###
pandoc \
    --template="$viewdir/template.html" \
    -f markdown_github+yaml_metadata_block "$md" |
    sed -r "/:\/\/|=\"\//!s;<(img src|a href)=\";&/$dir/;" |
    sed "s;/$dir/#;#;g"
