#!/usr/bin/env sh
# abort on errors
set -e
# build static files
yarn build
# navigate into the build output directory
cd dist
# create a fresh new git repo in the output directory
git init
git add -A
git commit -m 'deploy'
# Force push to the "publishing source" of your GitHub pages site
# in this case, the gh-pages branch
git push -f git@github.com:AVAST-Python/semana-1.git master:gh-pages
# Delete the temporary repo you created above
rm -Rf .git
# Back to previous directory (the root of your repo)
cd -
