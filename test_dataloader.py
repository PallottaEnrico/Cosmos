from nemo.collections.diffusion.train import videofolder_datamodule, pretrain

recipe = pretrain()

recipe.data = videofolder_datamodule()
recipe.data.path = ""  # path to folder with processed dataset


