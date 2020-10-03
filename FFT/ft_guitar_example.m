clear;clc;close all

% FOURIER ANALYSIS OF E2 STRING ON ELECTRIC GUITAR
% CODE AUTHORED BY: SHAWHIN TALEBI

% read audio file as array of amplitude values
[y, Fs] = audioread('Etest.WAV');

% peform fft
x = fft(y);

% get length of a audio file array
L = length(y);

% convert indicies to frequency values
f = Fs*(0:(L/2))/L;

% calculate power of frequency domain array
P2 = abs(x/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);

% plot original signal
subplot(2,1,1)
plot((1:length(y))/Fs, y, 'b-')
xlabel('Time')
ylabel('Voltage')

% format time domain plot
ax=gca;
ax.XLabel.String = 'Time (S)';
ax.XLabel.FontSize = 16;
ax.YLabel.String = 'Voltage';
ax.YLabel.FontSize = 16;

% plot signal in frequency domain
subplot(2,1,2)
plot(f(1:25000),P1(1:25000),'r-', 'LineWidth', 2);

% format frequency domain plot
ax=gca;
ax.XLabel.String = 'Frequency (Hz)';
ax.XLabel.FontSize = 16;
ax.YLabel.String = 'Power';
ax.YLabel.FontSize = 16;