import librosa
import librosa.display

import IPython.display as ipd

import numpy as np
import matplotlib.pyplot as plt

import os

file_path = 'Audio'

#wav만 가져오기
all_files = []
for root,dirs,files in os.walk(file_path):
    for file in files:
        if file.endswith('.wav'):
            all_files.append(os.path.join(root,file))

if len(all_files)==0:
    print("없음")
else:
    print("파일 개수 :",len(all_files))
#for i in all_files:
#    print(i)


#모든 파일 librosa 분석
for i in all_files:
    y, sr = librosa.load(i)
    plt.figure(figsize = (10,5))

    print()
    print('파일 이름 :',i,'진행상황 :',all_files.index(i)+1,"/",len(all_files))
    print('샘플 레이트 :',sr,'오디오 데이터 쉐입:',y.shape)
    print('길이 :', y.shape[0]/float(sr),'초')
    print()
    
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref = np.max)
    librosa.display.specshow(D, y_axis='linear', x_axis='time', sr=sr)

    plt.savefig("test/"+os.path.basename(i)[:-4]+".png")
    plt.close()


print("완료.")


'''
for i in all_files:
    #가져오기
    audio_path = i
    ipd.Audio(audio_path)

    #1초당 16000개 데이터 샘플링
    y, sr = librosa.load(audio_path,sr=16000)

    print('샘플 레이트:',sr,'오디오 데이터 쉐입:',y.shape)
    print('길이:', y.shape[0]/float(sr),'초')


    #3.STFT (Short-Time Fourier Transform) Spectogram

    n_fft = 1024 #fft 계산시 윈도우 크기 : 그냥 클수록 많이한다는 뜻 같음 높을수록 해상도 높아짐
    hop_length = 256 #한번 계산하고 이동하는 프레임 수: 작을수록 촘촘하게 하니 해상도가 높아짐

    stft = librosa.stft(y, n_fft = n_fft, hop_length = hop_length)
    spectrogram = np.abs(stft)
    print("Spectogram :\n", spectrogram)

    plt.figure(figsize = (10,5))
    librosa.display.specshow(spectrogram, sr=sr, x_axis='time',y_axis='linear', hop_length=hop_length,vmax=20)
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.grid(True)

    plt.plasma()
    plt.savefig("result/"+str(i)[6:]+".png")
    plt.close()

'''
