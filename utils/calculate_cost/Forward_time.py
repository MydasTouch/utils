# 计算reference正向耗时

from torch.profiler import profile, record_function, ProfilerActivity

activities = [ProfilerActivity.CUDA]
sort_by_keyword = "cpu" + "_time_total"
with profile(activities=activities, record_shapes=True) as prof:
    with record_function("model_inference"):
        model(mix.unsqueeze(0))
print(prof.key_averages().table(sort_by=sort_by_keyword, row_limit=10))
