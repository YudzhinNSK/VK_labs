filename = 'C:\Users\evgen\Documents\MATLAB\course\L256216.txt';
L256216 = importdata(filename);

close all;
nz = 5;  % center point
nr = 3;  % center point

ind_vals = [6]

for nphi=1:6
    test_sol216 = zeros(216, 1);
    ind_rzphi = [];
    ind_now = ind666(nz,nr,nphi);
    ind_vals(nphi) = ind_now;
    ind_rzphi = [ind_rzphi, ind_now]
    test_sol216(ind_rzphi) = 1;
    bsol216 = L256216 * test_sol216;
    bsol216sq = reshape(bsol216,16,16);
    figure
    pcolor(bsol216sq')
    colorbar
    xlabel('\it col')
    ylabel('\it row')
    title_str = strcat('Detector Matrix. Point nr =', num2str(nr),' nz =', num2str(nz), ' nphi=', num2str(nphi))
    title(title_str)
    fpath = 'C:\Users\evgen\Documents\MATLAB\course';
    saveas(gcf, fullfile(fpath, char(strcat(title_str, '.png'))), 'png'); 
end

%reverse task

for i = 1:length(ind_vals)
    n_z = round(ind_vals(i)/36);
    n_r = round((ind_vals(i) - 36 * (n_z - 1))/6);
    n_phi = ind_vals(i) - 36 * (n_z - 1) - 6 * (n_r - 1);
    fprintf('n_z = %d, n_r = %d, n_phi = %d\n', n_z, n_r, n_phi);
end