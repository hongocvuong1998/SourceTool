import librosa
import numpy as np
audio_path = './tmp/3.wav'
def audio2vector(audio_path):
    X ,sample_rate = librosa.load(audio_path,sr=44100)
    stft = np.abs(librosa.stft(X))
    # short term fourier transform
    chromastft = np.abs(librosa.stft(X))
    # mfcc (mel-frequency cepstrum)
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
    # chroma
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
    # melspectrogram
    mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
    # spectral contrast
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)


    audio_feature =np.concatenate((mfccs, chroma,mel,contrast,tonnetz))
    audio_feature = audio_feature-np.min(audio_feature)
    return audio_feature

# a= audio2vector(audio_path)

# print(a.shape)
t=  np.zeros((200))
t=t[0:192]
temp = np.tile(t,(10,1))
# # temp = np.repeat((t,10),axis=1)
# # n = np.stack(t,t)
# # test1 = np.zeros((10, 200) )

test2 = np.zeros((10, 2048))
# b=np.concatenate((test2,temp),axis=1)
b=(10,20)
print(type(b.shape))