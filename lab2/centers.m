X = intval([infsup(-512,512),infsup(-512, 512)]);
[Z, WorkList, diams] = globopt0(X);
solution = -959.6407;
centers_x= [];
centers_y = [];
for i = 1 : length(WorkList)
    centers_x(i) = WorkList(i).Box(1).mid;
    centers_y(i) = WorkList(i).Box(2).mid;
end
plot(centers_x(100:1001), centers_y(100:1001)); 
xlabel('Center X');
ylabel('Center Y');
title('Trajectory of bar center');
full_title = 'Trajectory_center';
saveas(gcf, fullfile(path, char(full_title)), 'png'); 