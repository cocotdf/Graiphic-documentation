<h1>Save ONNX File</h1>

<h2>Description</h2>

<p>This VI exports a model to a .onnx file. The generated file can be used to initialize an inference session. If training information is included during export, the file can also be used to initialize a training session.</p>

<p align="center"><img alt="save_onnx_file" src="/_assets/shared-images/c8/c8d540c2ea2a-save_onnx_file.png" width="220"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Model.Png" src="/_assets/shared-images/21/21498ef0ddd0-input_model.png" width="42"/></td>
      <td valign="top"><strong>Model in : </strong>reference to the model to save. This is an instance of the <code>Model</code> class of the LabVIEW Deep Learning Toolkit.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Path In.Png" src="/_assets/shared-images/37/37a46ccf5b9b-path-in.png" width="42"/></td>
      <td valign="top"><strong>File Path : <em>path</em>,</strong> destination path for the <code>.onnx</code> file to be written.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Enum.Png" src="/_assets/shared-images/9d/9d61ac752ae1-enum.png" width="42"/></td>
      <td valign="top"><strong>save : <em>enum,</em></strong>
<ul>
<li>
<ul>
<li><strong>Without Train Info</strong> : Exports a standard ONNX file, lightweight and compatible with inference sessions.</li>
<li><strong>With Train Info</strong> : Embeds training-related metadata (e.g., optimizer states, momentum buffers). The file size may increase by a few KBs for metadata, or significantly more (up to ×3) if momentum data is included.</li>
</ul>
</li>
</ul></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Model.Png" src="/_assets/shared-images/3c/3c881c79a647-output_model.png" width="42"/></td>
      <td valign="top"><strong>Model out : </strong>output reference of the model, allowing chaining.</td>
    </tr>
  </tbody>
</table>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
