import PyIO
import PyPluMA
import pickle
import pandas

class AttentionMergePlugin:
    def input(self, inputfile):
        self.files = PyIO.readSequential(inputfile)
    def run(self):
        pass
    def output(self, outputfile):
        file1 = open(PyPluMA.prefix()+"/"+self.files[0], "rb")

        attn_df_test = pickle.load(file1)
        scores_df = pandas.read_csv(PyPluMA.prefix()+"/"+self.files[1])
        attn_df_test = attn_df_test.merge(scores_df, on="PPI", how='left')
        outfile = open(outputfile, "wb")
        pickle.dump(attn_df_test, outfile)
        
