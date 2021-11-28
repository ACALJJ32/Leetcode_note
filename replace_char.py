class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """

        return s.replace(" ", "%20")  # 可以替换字符串


## C++ 版本:
####################################################
# class Solution {
# public:
#     string replaceSpace(string s) {
#         while(true) {
#             string::size_type space = s.find(" ");
#             if (space == s.npos) break;
#             else {
#                 s.replace(space, 1, "%20");
#             }
#         }
#         return s;
#     }
# };
####################################################

## C++ auto 系列 

####################################################
# class Solution {
# public:
#     string replaceSpace(string s) {
#         string result;
#         for (auto &c : s) {
#             if (c != ' ') result.push_back(c);
#             else{
#                 result.push_back('%');
#                 result.push_back('2');
#                 result.push_back('0');
#             }
#         }
#         return result;
#     }
# };
####################################################