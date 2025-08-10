% 讀取灰階影像
image = imread('D:/Edge Project/Processed Image/prcess_couple.jpg');
if size(image, 3) == 3
    image = rgb2gray(image);
end

% 二值化
binary = imbinarize(image);

% 定義 3×3 結構元素
se = strel('square', 3);

% Morph1：形態學 Opening（先腐蝕再膨脹）
morph1_result = imopen(binary, se);

% 顯示結果
figure;
subplot(1,2,1);
imshow(binary);
title('Original Binary');

subplot(1,2,2);
imshow(morph1_result);
title('Morph1 (Remove Isolated Pixels)');
