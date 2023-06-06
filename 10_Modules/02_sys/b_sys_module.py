import sys

print(dir(sys))

# sys.winver, sys.getwindowsversion()
print(
    f"""
    {sys.version            =}
    {sys.version_info       =}
    {sys.implementation     =}

    {sys.api_version        =}
    {sys.is_finalizing()    =}

    sys.copyright           =\n{sys.copyright}
"""
)
