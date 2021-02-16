clear; close all; clc

% CODE TO USE AUTOENCODERS TO REDUCE DIMENSIONALITY OF 64 ELECTRODE EEG
% DATA

% CODE AUTHORED BY: SHAWHIN TALEBI
% THE UNIVERSITY OF TEXAS AT DALLAS
% MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

%% DATA

% load data
load('EEG.mat')

% autoscale variables
X = ((EEG.Variables - mean(EEG.Variables))./std(EEG.Variables))';

%% PLOT SOME DATA

% pick electrodes at random and plot their voltagtime series
idx = randi(64,8,1);

fig = figure(1);
fig.Units = 'normalized';
fig.Position = [0 0 1 1];

for i = 1:length(idx)

    subplot(4,2,i)
    plot(X(idx(i),:))
    title(EEG.Properties.VariableNames(i), 'Fontsize', 16)
    ylabel('Autoscaled Voltage', 'Fontsize', 14)
    xlabel('Time Index', 'Fontsize', 14)

end
print('plots/electrode_timeseries', '-dpng')
%% AUTOENCODER

% define number of hidden neurons
q = 3;

% train autoencoder
autoenc = trainAutoencoder(X, q);

% use autoencoder net to predict X
predX = predict(autoenc, X);

% % encode input data
% Z = encode(autoenc, X)';

%% EVALUATE PERFORMANCE

% compare true and estimates voltage values
% plot same electrodes from earlier
fig = figure(2);
fig.Units = 'normalized';
fig.Position = [0 0 1 1];

for i = 1:8

    subplot(4,2,i)
    plot(X(idx(i),:))    
    hold on
    plot(predX(idx(i),:))
    title(strcat("Electrode ", EEG.Properties.VariableNames(i)), 'Fontsize', 16)
    ylabel('Autoscaled Voltage', 'Fontsize', 14)
    xlabel('Time Index', 'Fontsize', 14)

    legend('True Voltage', 'Estimated Voltage', ...
        'Location', 'bestoutside', 'Fontsize', 12)
end
print('plots/true_vs_est_electrode_timeseries', '-dpng')

% average all voltage values
X_agg = mean(X);
predX_agg = mean(predX);

% correlation coefficent between average voltage of true and estimated data
R = corrcoef(X_agg,predX_agg);
r2  = round(R(1,2)^2,3);

% create figure
fig = figure(3);
fig.Units = 'normalized';
fig.Position = [0 0 1 1];

% plot comparison of true and estimated averaged eeg voltages
scatterhist(X_agg,predX_agg)
hold on
plot([min(X_agg) max(X_agg)], [min(X_agg) max(X_agg)], ...
    'k--', 'Linewidth', 2)
legend("R^2= " + string(r2), '1:1', 'Location', 'southeast', 'FontSize' ,16)
axis tight
hold off
title('Performance of Aggregated Dynamics Estimation', 'FontSize',16)
xlabel('True Averaged Voltage (\muV)', 'FontSize' ,16)
ylabel('Estimated Averaged Voltage (\muV)', 'FontSize' ,16)

print('plots/true_vs_est_scatter_plot', '-dpng')