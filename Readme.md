# PointDreamer: 
This repository contains the official implementation for the anomyous under-review paper: PointDreamer: *''Zero-shot 3D Textured Mesh Reconstruction from Colored Point Cloud by 2D Inpainting''*.


## Install
We tested on torch2.0.0, cuda11.8. Other versions may also work.
```bash
# clone this repo
cd PointDreamer
conda create --name pointdreamer python=3.8
conda activate pointdreamer

pip install torch==2.0.0  torchvision==0.15.1 --index-url https://download.pytorch.org/whl/cu118
pip install kaolin==0.15.0 -f https://nvidia-kaolin.s3.us-east-2.amazonaws.com/torch-2.0.0_cu118.html
pip install git+https://github.com/NVlabs/nvdiffrast/
pip install https://data.pyg.org/whl/torch-2.0.0%2Bcu118/torch_cluster-1.6.3%2Bpt20cu118-cp38-cp38-linux_x86_64.whl
pip install requirements.txt
```

Download pretrained weights 'ShapeNet 3k, noise, no normals' of POCO, and put it like 'models/POCO/checkpoint.pth

```bash
wget https://github.com/valeoai/POCO/releases/download/v0.0.0/ShapeNet_3k.zip
unzip ShapeNet_3k.zip
mv XXX.pth models/POCO/checkpoint.pth
```

The pretrained weight of guided diffusion should be automatically downloaded when runnning demo.py.

## Usage
To run PointDreamer, use the following command:
```bash
python demo.py --config [CONFIG_FILE] --pc_file [PC_FILE]
```
- `[CONFIG_FILE]`: path to the configuration file, e.g. 'configs/default.yaml'
- `[PC_FILE]`: path to the input point cloud file (.ply), e.g. 'dataset/demo_data/clock.ply'

By default, the results will be saved at './output'. 
The reconstructed mesh will be saved at './output/name/models/model_normalized.obj'. Make sure to open it with the '.mtl' and '.png' file in the same folder. For example, use Meshlab or Blender to open it.
If you'd like to change the output directory, change the 'output_path' in the config file.

Here's some examples:
```bash
python demo.py --config configs/default.yaml --pc_file dataset/demo_data/clock.ply
python demo.py --config configs/default.yaml --pc_file dataset/demo_data/cup.ply
python demo.py --config configs/default.yaml --pc_file dataset/demo_data/PaulFrankLunchBox.ply
python demo.py --config configs/default.yaml --pc_file dataset/demo_data/rolling_lion.ply

python demo.py --config configs/default.yaml --pc_file dataset/NBF_demo_data/2ce6_chair.ply
python demo.py --config configs/default.yaml --pc_file dataset/NBF_demo_data/70aa_chair.ply
python demo.py --config configs/wo_NBF.yaml --pc_file dataset/NBF_demo_data/2ce6_chair.ply
python demo.py --config configs/wo_NBF.yaml --pc_file dataset/NBF_demo_data/70aa_chair.ply
```

## Output
TODO


## Acknolwedgement
This work is built upon DDNM, POCO, and GET3D. Thank the authors for thier amazing work!