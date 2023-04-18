from nomic.gpt4all import GPT4AllGPU

LLAMA_PATH = "gpt4all-lora-quantized.bin"

m = GPT4AllGPU(LLAMA_PATH)
config = {'num_beams': 2,
          'min_new_tokens': 10,
          'max_length': 100,
          'repetition_penalty': 2.0}

while True:
    out = m.generate(input(), config)
    print(out)
