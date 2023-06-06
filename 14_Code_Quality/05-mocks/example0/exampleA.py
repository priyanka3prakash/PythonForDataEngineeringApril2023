from unittest.mock import Mock

mock = Mock()
print(mock)

print(f"{mock.name          =}")
print(f"{mock.age           =}")
print(f"{mock.salary        =}")
print(f"{mock.absent_days   =}")
print(f"{mock.roles         =}")
print()



mock = Mock(
    name="Udhay",
    age=25,
    salary=123123123.123,
    absent_days=None,
    roles=["SE", "Architect"],
)
print(mock)

print(f"{mock.name          =}")
print(f"{mock.age           =}")
print(f"{mock.salary        =}")
print(f"{mock.absent_days   =}")
print(f"{mock.roles         =}")

print(f"\n{mock.return_value  =}")

# calling Undefined attributes
print(f"\n{mock.return_values =}")
print(f"{mock.something     =}")
print()

mock = Mock(return_values=10)
mock(1)
mock(1, 4)
mock(1, 4, foo="bar")


print(f"\n{mock.return_value  =}")
print(f"{mock.return_values =}")
print(f"{mock.call_count    =}")
print(f"{mock.call_args     =}")
print(f"{mock.call_args_list=}")
print(f"{mock.called        =}")
print(f"{mock.mock_calls    =}")

print(mock.assert_called())

mock = Mock(side_effect=KeyError("foobar"))
print(f"\n{mock.side_effect   =}")
try:
    mock()
except KeyError as ex:
    print(repr(ex))

# print(dir(mock))
# ['assert_any_call', 'assert_called', 'assert_called_once',
# 'assert_has_calls', 'assert_not_called', 'attach_mock',
# 'method_calls', 'mock_add_spec', 'mock_calls']
