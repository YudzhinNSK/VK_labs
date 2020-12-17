%x = infsup(-5,5);
%y = infsup(-5,5);
x=infsup(-10,10);
y=infsup(-10,10);
z = globopt0([x,y]);

for i = 1:1000
    disp(i);
    answer = z(i).Estim;
    disp(answer);
    xl = z(i).Box(1).inf;
    xr = z(i).Box(1).sup;
    yl = z(i).Box(2).inf;
    yr = z(i).Box(2).sup;
    rectangle('Position',[xl yl xr-xl yr-yl]);
end
%axis([-8 8 -8 8])
axis([-12 12 -12 12])

X = intval([infsup(-512,512),infsup(-512, 512)]);
WorkList = globopt0(X);
solution = -959.6407;

answer = [];
for i = 1 : length(WorkList)
    answer(i) = WorkList(i).Estim;
end

for i = 1:length(answer)
    diff(i) = abs(answer(i) - solution);
end
iter = 1:1:length(answer);
plot(iter, diff);

semilogx(iter, diff);
hold on;
xlim([0, length(answer)]);
xlabel('Iterations');
ylabel('Absolute difference');
title('Convergence of method');
path = 'C:\Users\evgen\Documents\MATLAB';
full_title = 'EggholderLog';
saveas(gcf, fullfile(path, char(full_title)), 'png'); 