# 这个计算方法是基于Asteroid，一般是在测试（reference）时候（eval.py）中进行计算。

# pip install ptflops

# model_path = os.path.join(conf["exp_dir"], "best_model.pth")
# model = real_SepFormer.from_pretrained(model_path)
# if conf["use_gpu"]:
#     model.cuda()
# model_device = next(model.parameters()).device
from ptflops import get_model_complexity_info
macs, params = get_model_complexity_info(model, (1, 24000), as_strings=True,
                                        print_per_layer_stat=True, verbose=True)


print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
print('{:<30}  {:<8}'.format('Number of parameters: ', params))
