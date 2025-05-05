# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

aws s3 sync $SCRIPT_DIR/../../dist s3://codereimaginedtypingappaws-s3bucketroot-e9cabqeshsne --delete
