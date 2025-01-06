export NCCL_P2P_DISABLE=1
export NCCL_IB_DISABLE=1

llamafactory-cli train examples/train_qlora/qwen_lora_sft_bitsandbytes.yaml >> logs/train/train_14b_ar_e5.log 2>&1