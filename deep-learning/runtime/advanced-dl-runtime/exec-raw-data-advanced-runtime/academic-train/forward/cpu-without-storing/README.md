<h1>Inputs CPU Raw Data (without storing)</h1>

<h2>Description</h2>

<p>Run the forward model with the raw input data from the CPU, the output buffer is allocated automatically. Inputs and Outputs are stored inside Academic Training Session (we can’t execute backward).</p>

<p align="center"><img alt="academic_fw_cpu_2" src="/_assets/shared-images/48/48519cd27fd9-academic_fw_cpu.png" width="220"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Academic.Png" src="/_assets/shared-images/03/039f017e9f6f-input_academic.png" width="42"/></td>
      <td valign="top"><strong>Academic Training in</strong> <strong>: <em>object, </em></strong>academic training session.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="32"/><strong>Inputs Info : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Unsigned_8.Png" src="/_assets/shared-images/f7/f7e8b09da0a0-input_array_unsigned_8.png" width="42"/></td>
      <td valign="top"><strong>inputs_data : <em>array, </em></strong>contains the raw byte representation of the input tensor data, stored as a 1D flattened buffer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_64.Png" src="/_assets/shared-images/71/712313814f21-input_array_integer_64.png" width="42"/></td>
      <td valign="top">inputs_shapes :<em> array, </em>specifies the shape of the input tensor. Since the data is stored as a flattened 1D buffer, this shape is necessary to reconstruct the original dimensions.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_64.Png" src="/_assets/shared-images/71/712313814f21-input_array_integer_64.png" width="42"/></td>
      <td valign="top">inputs string length : <em>array, </em>used when the tensor type is string. If the tensor has shape <code>[5,3]</code>, this field contains 15 values, each representing the length of a corresponding string element. This ensures that the actual size of <code>inputs_data</code> is known despite variable string lengths.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_64.Png" src="/_assets/shared-images/71/712313814f21-input_array_integer_64.png" width="42"/></td>
      <td valign="top">inputs_ranks :<em> array, </em>indicates the rank of the tensor, i.e. the number of dimensions (Scalar = 0, 1D = 1, 2D = 2, etc.).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Enum.Png" src="/_assets/shared-images/05/05126b56ff83-input_array_enum.png" width="42"/></td>
      <td valign="top">inputs_types :<em> array, </em>defines the ONNX tensor type as an enumerated value (e.g. FLOAT, INT64, STRING).</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="input_param_inference_forward_cpu" src="/_assets/shared-images/4f/4ff07b637a4b-input_param_inference_forward_cpu.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Academic.Png" src="/_assets/shared-images/85/85272a982dfe-output_academic.png" width="42"/></td>
      <td valign="top"><strong>Academic Training out</strong> <strong>: <em>object, </em></strong>academic training session.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Cluster Out.Png" src="/_assets/shared-images/0a/0a479d27b394-cluster-out.png" width="32"/><strong>Losses Info : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Unsigned_8.Png" src="/_assets/shared-images/ee/eeb63aea4468-output_array_unsigned_8.png" width="42"/></td>
      <td valign="top"><strong>outputs_raw_data : <em>array, </em></strong>contains the raw byte representation of the input tensor data, stored as a 1D flattened buffer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_64.Png" src="/_assets/shared-images/8a/8a3ecb76444e-output_array_integer_64.png" width="42"/></td>
      <td valign="top">output_shapes_array :<em> array, </em>specifies the shape of the input tensor. Since the data is stored as a flattened 1D buffer, this shape is necessary to reconstruct the original dimensions.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_64.Png" src="/_assets/shared-images/8a/8a3ecb76444e-output_array_integer_64.png" width="42"/></td>
      <td valign="top">output_strings_length_array : <em>array, </em>used when the tensor type is string. If the tensor has shape <code>[5,3]</code>, this field contains 15 values, each representing the length of a corresponding string element. This ensures that the actual size of <code>inputs_data</code> is known despite variable string lengths.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_64.Png" src="/_assets/shared-images/8a/8a3ecb76444e-output_array_integer_64.png" width="42"/></td>
      <td valign="top">output_ranks_array :<em> array, </em>indicates the rank of the tensor, i.e. the number of dimensions (Scalar = 0, 1D = 1, 2D = 2, etc.).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Out Array Integer 32.Png" src="/_assets/shared-images/fe/fe7405762e7c-output_array_integer_32.png" width="42"/></td>
      <td valign="top">output_types_array :<em> array, </em>defines the ONNX tensor type as an enumerated value (e.g. FLOAT, INT64, STRING).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String_Array_Out.Png" src="/_assets/shared-images/43/43e33de4b021-output_array_string.png" width="42"/></td>
      <td valign="top"><strong>losses_names : <em>array,</em></strong> specifies which loss the data correspond to.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="output_param_training_full_train_step_cpu" src="/_assets/shared-images/ba/ba1e285bfea1-output_param_training_full_train_step_cpu.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
