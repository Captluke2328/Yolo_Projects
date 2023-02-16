## To enable GPU acceleration
1. download vscommunity and download 
2. download CUDA Toolkit. In my case, i'm using Version 11 and download exe(local)
3. download NVIDIA cuDNN (you may need to sign in to download this package).
4. Once down copy the bin, include and bin files into CUDA directory which can be found in NVIDIA GPU Computing program files ../CUDA/version
5. Uninstall all installed pytorch using pip uninstall torch, torchvision and torchaudio to prevent the conflict with cuda version
6. Go to https://pytorch.org/get-started/locally/ and select pip, cuda 11.6 and copy pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116 into terminal
7. You're done !