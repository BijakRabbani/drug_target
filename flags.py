from arguments import argparser

FLAGS = argparser()
FLAGS.num_windows = [32]
FLAGS.seq_window_lengths = [8]
FLAGS.smi_window_lengths = [8]
FLAGS.batch_size = 256
FLAGS.num_epoch = 100
FLAGS.max_seq_len = 1200
FLAGS.max_smi_len = 85
FLAGS.dataset_path = 'data/davis/'
FLAGS.problem_type = 1
FLAGS.log_dir = 'logs/'

