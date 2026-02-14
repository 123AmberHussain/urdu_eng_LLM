import torch
import sys

print(f"Python version: {sys.version}")
print(f"PyTorch version: {torch.__version__}")

if torch.cuda.is_available():
    print(f"✅ NVIDIA GPU Detected: {torch.cuda.get_device_name(0)}")
    print(f"CUDA Version: {torch.version.cuda}")
elif torch.backends.mps.is_available():
    print("✅ Apple Silicon (M-series) GPU Detected")
else:
    print("❌ No GPU found. We'll use the CPU for now (good for logic, slow for training).")