mkdir -p /tmp/synData

scp -r ./Synthetic_images1/shuriken_[0-9][0-9].jpg /tmp/synData
scp -r ./Synthetic_images1/shuriken_[0-9].jpg /tmp/synData

scp -r ./Synthetic_images1/rajor\ blade_[0-9][0-9].jpg /tmp/synData
scp -r ./Synthetic_images1/rajor\ blade_[0-9].jpg /tmp/synData

scp -r ./Synthetic_images1/knife_[0-9][0-9].jpg /tmp/synData
scp -r ./Synthetic_images1/knife_[0-9].jpg /tmp/synData

scp -r ./guns_images/*.jpg /tmp/synData

scp -r ./labels.csv /tmp/synData
scp -r ./labels_gun.csv /tmp/synData


scp -r ./test.py /tmp/synData
scp -r ./testGun.py /tmp/synData

rm -rf  /tmp/synData/*[0-9].txt

cd /tmp/synData/
python3.6 testGun.py
python3.6 test.py
