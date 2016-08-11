#!/usr/bin/env bash
set -e

function caption() {

    local model=${1:-'models/neuraltalk2_model.t7'}
    local image_folder=${2:-'images'}

    if [ VERBOSE = 1 ]; then
        printf "Variables:\n----------------------\n"
        printf "model         -> %s\n" "${model}"
        printf "image_folder  -> %s\n\n" "${image_folder}"
    fi

    cd neuraltalk2 && th eval.lua -num_images -1 -gpuid -1 \
        -model ../"${model}" \
        -image_folder ../"${image_folder}"
}

declare -i VERBOSE=0
while getopts ":vh" OPTION; do
    case ${OPTION} in
        v) VERBOSE=1
           ;;
       \?) echo "Invalid option: -${OPTARG}" >&2
           exit 1
           ;;
    esac
done
    shift $(($OPTIND-1))

if [ $0 = "${BASH_SOURCE}" ]; then
    caption $@
fi
