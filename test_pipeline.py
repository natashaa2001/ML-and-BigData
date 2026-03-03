import unittest
class TestPipeline(unittest.TestCase):
    def test_data_exists(self):
        import os
        self.assertTrue(os.path.exists('data/samples'))
    def test_spark_session(self):
        try:
            from pyspark.sql import SparkSession
            spark=SparkSession.builder.master('local').getOrCreate()
            spark.stop()
            self.assertTrue(True)
        except:
            self.fail('Spark failed')
if __name__=='__main__':
    unittest.main()
