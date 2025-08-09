% 主程式：載入影像並比較兩個方向的 edge fitting 結果
img = imread('D:/Edge Project/Gray Photo/gray_couple.jpg'); % 載入灰階影像
if size(img, 3) == 3
    img = rgb2gray(img); % 若為彩色則轉灰階
end

% 定義兩個方向
theta1 = pi/4;   % 45 度
theta2 = -pi/4;  % -45 度

% 執行 edge fitting
edge_map1 = edgefit(img, theta1);
edge_map2 = edgefit(img, theta2);

% 合併兩方向結果
combined_edge = edge_map1 | edge_map2;

% 顯示所有結果
figure;
subplot(2, 2, 1);
imshow(img, []);
title('Original Image');

subplot(2, 2, 2);
imshow(edge_map1);
title('\theta = \pi/4');

subplot(2, 2, 3);
imshow(edge_map2);
title('\theta = -\pi/4');

subplot(2, 2, 4);
imshow(combined_edge);
title('Combined Edge Map');

% 函式定義：edgefit
function edge_map = edgefit(image, theta)
    % image: 灰階影像矩陣
    % theta: 邊緣方向角度（以弧度為單位，例如 pi/4）

    % Step 1: 建立 5x5 的 x 和 y 階梯矩陣
    x = repmat([-2 -1 0 1 2], 5, 1);
    y = repmat([-2; -1; 0; 1; 2], 1, 5);

    % Step 2: 建立 edge fitting matrix s(x, y)
    s = double((x * cos(theta) + y * sin(theta)) < 0);

    % Step 3: 對影像進行卷積
    edge_response = conv2(double(image), s, 'same');

    % Step 4: 將結果二值化（可根據需求調整 threshold）
    threshold = graythresh(edge_response); % 使用 Otsu 方法自動選擇
    edge_map = edge_response > threshold * max(edge_response(:));
end
