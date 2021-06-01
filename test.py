from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer

paths = ["text_data.txt"]

tokenizer = GPT2Tokenizer.from_pretrained('tokenizer')

tokenizer.add_special_tokens({
	"eos_token": "</s>",
	"bos_token": "<s>",
	"unk_token": "<unk>",
	"pad_token": "<pad>",
	"mask_token": "<mask>",
	})

config = GPT2Config(
	vocab_size = tokenizer.vocab_size,
	bos_token = tokenizer.bos_token_id,
	eos_token = tokenizer.eos_token_id,
	)

model = GPT2LMHeadModel.from_pretrained("Python_auto").to("cuda")

NEWLINECHAR='<N>'
def encode_newlines(inp):
	return inp.replace("\n", NEWLINECHAR)

def decode_newlines(inp):
	return inp.replace(NEWLINECHAR, "\n")


def auto_complete(inp):
	inp=encode_newlines(inp)

	input_tokens = tokenizer.encode(inp, return_tensors="pt").to("cuda")

	newline_count = inp.count(NEWLINECHAR)

	model_out = model.generate(
		input_tokens,
		max_length = 100,
		num_beams = 3,
		temperature =0.7,
		no_repeat_ngram_size = 5,
		num_return_sequences = 3,
		return_dict_in_generate = True,
		output_scores = True)

	sequence=model_out['sequences'][0]

	decoded = decode_newlines(tokenizer.decode(sequence))

	auto_comp = ""

	split = decoded.split('\n')

	for s in split[:newline_count+1]:
		auto_complete += s + '\n'
	return auto_comp

inp=" import numpy as "

output=auto_complete(inp)
print(output)

