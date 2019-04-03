#include <string>
#include "google/protobuf/util/json_util.h"
#include "google/protobuf/util/message_differencer.h"
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

  printf("\n%zu bytes\n", binary_payload.size());
  for(auto& chr : binary_payload)
    printf("%#x ", +static_cast<unsigned char>(chr));
  
  printf("\n%zu bytes\n", plain_text_payload.size());
  printf("%s", plain_text_payload.c_str());

  Bar parsed_message_from_binary;
  parsed_message_from_binary.ParseFromString(binary_payload);

  Bar parsed_message_from_plain_text;
  google::protobuf::util::JsonStringToMessage(plain_text_payload, &parsed_message_from_plain_text);

  assert(google::protobuf::util::MessageDifferencer::Equals(parsed_from_binary, parsed_message_from_plain_text));

  return 0;
}