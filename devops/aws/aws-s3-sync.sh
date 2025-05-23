
# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd $SCRIPT_DIR/../..
npm run build

aws s3 sync $SCRIPT_DIR/../../dist s3://codereimaginedtypingappaws-s3bucketroot-e9cabqeshsne --delete

aws cloudfront create-invalidation \
  --distribution-id E2VCVQ341CFRK1 \
  --paths "/*"
