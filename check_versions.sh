#!/bin/bash

release_version=`grep version setup.py | cut -d\' -f2`
versions=(
`node -p -e "require('./npm-packages/pyoes/package.json').version"`
`node -p -e "require('./pyoes/static/package.json').version"`
`node -p -e "require('./package.json').version"`
)

for i in "${versions[@]}"; do
    if [[ $release_version != $i ]]; then
        not_equal=true
        break
    fi
done

[[ -n "$not_equal" ]] && echo "Not all version strings match release_version $release_version" && exit 1
exit 0
