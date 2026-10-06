FROM vllm/vllm-openai:latest
ENV MODEL_NAME Qwen/Qwen2.5-7B-Instruct
ENTRYPOINT python3 -m vllm.entrypoints.openai.api_server --model $MODEL_NAME $VLLM_ARGS
