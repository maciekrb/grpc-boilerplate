======================
Building gRPC Services
======================

This repo is an attempt to summarize some best practices around building gRPC 
services. 

You will find a sample service proto structure repository in ``sampleapis`` folder, 
the purpose is to define the service and message structure to use in the language
specific boilerplates around the services. 

For a complete reference of how different services can be structured, see 
`Google's service repository <https://github.com/googleapis/googleapis>`_ 
for gRPC services.

The language folders contain implementations of the sample service 
applying different techniques when building gRPC services in different
languages. 

Consider `Google's API design guide <https://cloud.google.com/apis/design/standard_fields>`_ 
for over all best practices when desing APIs.

See `Markdown and RST <https://gist.github.com/dupuy/1855764>`_ for choices around 
documentation tools. 
