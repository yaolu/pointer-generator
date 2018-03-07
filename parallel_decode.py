import tensorflow as tf
import os

FLAGS = tf.app.flags.FLAGS

# Where to find data
tf.app.flags.DEFINE_string('vocab_path', '', 'Path expression to text vocabulary file.')
tf.app.flags.DEFINE_string('log_root', '', 'Root directory for all logging.')
tf.app.flags.DEFINE_string('data_path', '', 'test data dir')

def main(unused_argv):
	if FLAGS.vocab_path == '' or FLAGS.log_root == '' or FLAGS.data_path == '':  # prints a message if you've entered flags incorrectly
		raise Exception("Please input cmd: python parallel_decode.py --vocab_path=path_to_vocab --log_root=path_to_log_root --data_path=../model_data/gan/")
	test_file = [os.path.join(FLAGS.data_path,elem) for elem in os.listdir(FLAGS.data_path) if 'test_0' in elem]
#	test_file = [os.path.join(FLAGS.data_path,'test_000.bin'), os.path.join(FLAGS.data_path,'test_001.bin'), os.path.join(FLAGS.data_path,'test_002.bin'), os.path.join(FLAGS.data_path,'test_003.bin')]
	cmd = []
	for elem in test_file:
		cmd.append('sleep 1.2; python run_summarization.py --mode=decode --beam_size 5 --data_path {} --vocab_path {} --log_root {} --single_pass 1 --coverage False --max_dec_steps 120'.format(elem, FLAGS.vocab_path, FLAGS.log_root))
	parallel_cmd = ' & '.join(cmd)

#	cmd0 = 'sleep 0.2; python run_summarization.py --mode=decode --beam_size 5 --data_path {} --vocab_path {} --log_root {} --single_pass 1 --coverage False --max_dec_steps 120'.format(test_file[0], FLAGS.vocab_path, FLAGS.log_root)

#	parallel_cmd = cmd0 + " & " + cmd1 + " & " + cmd2 + " & " + cmd3

	os.system(parallel_cmd)

if __name__ == '__main__':
    tf.app.run()
