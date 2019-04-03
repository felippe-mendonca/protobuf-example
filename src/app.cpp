#include <iostream>
#include <string>
#include "google/protobuf/util/json_util.h"
#include "message.pb.h"

int main() {

  Bar message;
  message.mutable_foo()->set_integer_field(10);
  message.mutable_foo()->set_str_field("asdfg");
  message.set_baz("qwert");

  std::string binary_payload;
  message.SerializeToString(&binary_payload);

  std::string plain_text_payload;
  google::protobuf::util::JsonPrintOptions options;
  options.always_print_primitive_fields = true;
  google::protobuf::util::MessageToJsonString(message, &plain_text_payload, options);

  std::cout << binary_payload.size() << " bytes\n" << binary_payload << std::endl;
  std::cout << plain_text_payload.size() << " bytes\n" << plain_text_payload << std::endl;

  return 0;

}