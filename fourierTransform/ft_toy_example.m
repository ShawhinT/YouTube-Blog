clear;clc;close all

% TOY FOURIER TRANSFORM EXAMPLE
% CODE AUTHORED BY: SHAWHIN TALEBI

% define signal
f = @(x) sin(x)+sin(2*x);
Fs = 10000;
numPeriods = 7;
x = linspace(0,2*pi*numPeriods,Fs*numPeriods);
y = f(x);

% peform fft
x = fft(y);

% get length of a audio file array
L = length(y);
% convert indicies to frequency values
k = Fs*(0:(L/2))/L;

% calculate power of frequency domain array
P2 = abs(x/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);

% plot original signal
subplot(2,1,1)
t = ((1:L)-1)/Fs;
plot(t, y, 'b-')

% format time domain plot
ax=gca;
ax.XLabel.String = 'Time (S)';
ax.XLabel.FontSize = 16;
ax.YLabel.String = 'Amplitude';
ax.YLabel.FontSize = 16;

% plot signal in frequency domain
subplot(2,1,2)
plot(k(1:25),P1(1:25),'r-', 'LineWidth', 2);

% format frequency domain plot
ax=gca;
ax.XLabel.String = 'Frequency (Hz)';
ax.XLabel.FontSize = 16;
ax.YLabel.String = 'Coefficent';
ax.YLabel.FontSize = 16;

% print figure to file
print('ft_toy_exmaple', '-dpng');