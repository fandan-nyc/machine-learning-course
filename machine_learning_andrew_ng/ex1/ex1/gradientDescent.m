function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training eXamples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
%    disp("theta is: "), disp(theta); 
   % solution 1:
   % theta0 = theta(1) - 1 / m * alpha * sum((X * theta - y) .* X(:,1));
   % theta1 = theta(2) - 1 / m * alpha * sum((X * theta - y) .* X(:,2));
   % theta = [theta0; theta1];
   % end of solution1 
   % solution 2: vectorization
    theta = theta - 1 / m * alpha * ((X * theta - y)' * X)';
%    display("theta0 is:"), disp(theta0);
%   display("theta1 is:"), disp(theta1);
%    disp("tmp1 is: "), disp(tmp1), disp("tmp2 is:"), disp(tmp2), disp("theta is: "), disp(theta);
    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);
%    disp(J_history)
end

end
