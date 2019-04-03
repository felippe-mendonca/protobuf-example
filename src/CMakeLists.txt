include(GNUInstallDirs)

find_package(Protobuf REQUIRED)

PROTOBUF_GENERATE_CPP(message_src message_hdr message.proto)

add_executable(app.bin app.cpp ${message_src} ${message_hdr})
target_link_libraries(app.bin PRIVATE protobuf::libprotobuf)
target_include_directories(app.bin PRIVATE  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>)
set_property(TARGET app.bin PROPERTY CXX_STANDARD 11)