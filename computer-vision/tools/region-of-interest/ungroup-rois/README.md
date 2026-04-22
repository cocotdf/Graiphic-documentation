<h1>Ungroup ROIs</h1>

<h2>Description</h2>

<p>Separates an ROI descriptor describing many contours into an array of ROI descriptors. Each of the ROI descriptors returned contains a single contour. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/3b/3b91a8dd58f7-ungroup_roi.png" alt="Ungroup_Roi.Png" width="289" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Cluster_2.Png" src="/_assets/shared-images/ab/ab143124dd51-input_cluster_2.png" width="42"/></td>
      <td valign="top"><strong>ROI Descriptor : <em>cluster, </em></strong>descriptor that contains multiple contours.</td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_32.Png" src="/_assets/shared-images/05/052f6e6ea35b-input_array_integer_32.png" width="42"/></td>
      <td valign="top"><strong>Global Rectangle : <em>array, </em></strong>minimum rectangle required to contain all of the contours in the ROI.  Rectangles are specified by their bounding rectangle, with the format (Left/Top/Right/Bottom).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Cluster_2.Png" src="/_assets/shared-images/7c/7c2884d81fe7-cluster-array-in.png" width="42"/></td>
      <td valign="top"><strong>Contours : <em>array, </em></strong>are each of the individual shapes that define an ROI.</td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Enum.Png" src="/_assets/shared-images/5c/5c2b52d3b208-input_enum.png" width="42"/></td>
      <td valign="top"><strong>ID : <em>enum, </em></strong>refers to whether the contour is the external or internal edge of an ROI.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Unsigned_16.Png" src="/_assets/shared-images/f6/f63ea71f0ad0-input_unsigned_16.png" width="42"/></td>
      <td valign="top"><strong>Type : <em>integer, </em></strong>is the shape type of the contour.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_32.Png" src="/_assets/shared-images/05/052f6e6ea35b-input_array_integer_32.png" width="42"/></td>
      <td valign="top"><strong>Coordinates : <em>array, </em></strong>indicates the relative position of the contour.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img src="/_assets/shared-images/bc/bcf3bfc6fa59-input_roi_descriptor.png" alt="input_roi_descriptor" width="231" /></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Ouput_Array_Cluster_2.Png" src="/_assets/shared-images/ce/ce79fc3283cc-cluster-array-out.png" width="42"/></td>
      <td valign="top"><strong>ROI Descriptors : <em>array, </em></strong>returned array of ROI descriptors. Each ROI descriptor contains a single contour.</td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_32.Png" src="/_assets/shared-images/fe/fe7405762e7c-output_array_integer_32.png" width="42"/></td>
      <td valign="top"><strong>Global Rectangle : <em>array, </em></strong>contains the coordinates of the bounding rectangle. Rectangles are specified by their bounding rectangle, with the format (Left/Top/Right/Bottom).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Ouput_Array_Cluster_2.Png" src="/_assets/shared-images/ce/ce79fc3283cc-cluster-array-out.png" width="42"/></td>
      <td valign="top"><strong>Contours : <em>array, </em></strong>are each of the individual shapes that define an ROI.</td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Enum.Png" src="/_assets/shared-images/a0/a0e1d8d91545-output_enum.png" width="42"/></td>
      <td valign="top"><strong>ID : <em>enum, </em></strong>refers to whether the contour is the external or internal edge of an ROI.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Unsigned_16_.Png" src="/_assets/shared-images/b5/b5a6a12a295e-output_unsigned_16_.png" width="42"/></td>
      <td valign="top"><strong>Type : <em>integer, </em></strong>is the shape type of the contour.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_32.Png" src="/_assets/shared-images/fe/fe7405762e7c-output_array_integer_32.png" width="42"/></td>
      <td valign="top"><strong>Coordinates : <em>array, </em></strong>indicates the relative position of the contour.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img src="/_assets/shared-images/74/74354d5430f5-input_roi_descriptors.png" alt="input_roi_descriptors" width="260" /></p></td>
    </tr>
  </tbody>
</table>

<h2>Examples</h2>

<p>All these examples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Computer Vision ​library to run it).</p>
