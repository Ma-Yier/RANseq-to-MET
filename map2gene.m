function [line] = map2gene(inputFile,outputFile)

load("./genelist_hashmap.mat");
fid_in = fopen(inputFile, 'r');
if fid_in == -1
    error('无法打开输入文件: %s', inputFile);
end

fid_out = fopen(outputFile, 'w');
if fid_out == -1
    fclose(fid_in);
    error('无法创建输出文件: %s', outputFile);
end

line = fgetl(fid_in);
while ischar(line)
    if isKey(dataMap, line)
        line = dataMap(line);
    end
    fprintf(fid_out, '%s\n', line);
    line = fgetl(fid_in);
end

fclose(fid_in);
fclose(fid_out);

disp('文件复制完成！');
end

