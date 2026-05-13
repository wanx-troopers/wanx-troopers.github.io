import safetensors.torch
sd = safetensors.torch.load_file(input("Enter path to lora: "))
sd_out = {}

for k in sd:
  sd_out["diffusion_model.{}".format(k.replace("base_model.model.", "").replace("lora_down", "lora_A").replace("lora_up", "lora_B").replace("lora_unet_", "").replace("_blocks_", "_blocks.").replace("_img_", ".img_").replace("_txt_", ".txt_").replace("_linear_", ".linear_").replace(".down.weight", ".lora_down.weight").replace(".up.weight", ".lora_up.weight").replace(".processor.proj_lora1.", ".img_attn.proj.").replace(".processor.proj_lora2.", ".txt_attn.proj.").replace(".processor.qkv_lora1.", ".img_attn.qkv.").replace(".processor.qkv_lora2.", ".txt_attn.qkv."))] = sd[k]

safetensors.torch.save_file(sd_out, "converted_lora.safetensors")
