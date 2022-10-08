#include "pch.h"
#include "CppUnitTest.h"


#include "../Linkedlist.h"
#include "../Node.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;


/*
				Instructions

Test -> Test Explorer || Right click project file and click "run tests'

Resolve linking issues: https://docs.microsoft.com/en-us/visualstudio/test/how-to-use-microsoft-test-framework-for-cpp?view=vs-2019#object_files

*/

namespace LinkedListUnitTests
{
	TEST_CLASS(LinkedListUnitTests)
	{
	public:

		TEST_METHOD(TestInsertingToHead)
		{	
			Linkedlist linked_list = Linkedlist();
			Assert::AreEqual(linked_list.size, 0);

			Node n_1(0);
			linked_list.insert_to_head(&n_1);
			Assert::AreEqual(linked_list.size, 1);

			linked_list.insert_to_head(10);
			Assert::AreEqual(linked_list.size, 2);
		}
		
		TEST_METHOD(TestRemovingNodes)
		{
			Linkedlist linked_list = Linkedlist();
			Assert::AreEqual(linked_list.size, 0);

			Node n_1(0);
			linked_list.insert_to_head(&n_1);
			Assert::AreEqual(linked_list.size, 1);

			linked_list.insert_to_head(10);
			Assert::AreEqual(linked_list.size, 2);
			
			/* Add three more 10's */
			linked_list.insert_to_head(10);
			linked_list.insert_to_head(10);
			linked_list.insert_to_head(10);
			Assert::AreEqual(linked_list.size, 5);
			
			/* Remove all 10's */
			linked_list.remove_nodes_with_value(10);
			auto ll_iter = linked_list.iter_values();
			Assert::IsTrue(std::count(ll_iter.begin(), ll_iter.end(), 10) == 0);
		}
	};
}
