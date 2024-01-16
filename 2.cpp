/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(l1->val + l2->val);
        ListNode* latest = head;
        int carry = 0;
        // if (head->val >= 10) {
        //     carry = 1;
        //     head->val -= 10;
        // }
        // l1 = l1->next;
        // l2 = l2->next;
        while ((l1 != nullptr) || (l2 != nullptr)) {
            if ((l1->next != nullptr) || (l2->next != nullptr) || (carry > 0)) {
                latest->next = new ListNode();
                latest = latest->next;
            }
            int digit_sum = 0;
            if (l1 != nullptr) {
                digit_sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                digit_sum += l2->val;
                l2 = l2->next;
            }
            latest->val = carry + digit_sum;
            if (latest->val >= 10) {
                carry = 1;
                latest->val -= 10;
            } else {
                carry = 0;
            }
        }
        return head;
        // long l1_num = 0;
        // long l2_num = 0;
        // long l1mul = 1;
        // while (l1 != nullptr) {
        //     l1_num += (l1mul*l1->val);
        //     l1mul *= 10;
        //     l1 = l1->next;
        // }
        // long l2mul = 1;
        // while (l2 != nullptr) {
        //     l2_num += (l2mul*l2->val);
        //     l2mul *= 10;
        //     l2 = l2->next;
        // }
        // long total = l1_num + l2_num;
        // ListNode* l3 = new ListNode();
        // ListNode* l3head = l3;
        // while (total > 0) {
        //     l3->val = total % 10;
        //     total = total/10;
        //     if (total > 0) {
        //         l3->next = new ListNode();
        //     }
        //     l3 = l3->next;
        // }
        // return l3head;
    }
};