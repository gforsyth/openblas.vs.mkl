for i in range(1,9):
    $OPENBLAS_NUM_THREADS=i
    /home/gil/anaconda/bin/python mattest.py openblas OPENBLAS_NUM_THREADS

for i in range(1,9):
    $MKL_NUM_THREADS=i
    /home/gil/intelpython/bin/python3 mattest.py mkl MKL_NUM_THREADS
